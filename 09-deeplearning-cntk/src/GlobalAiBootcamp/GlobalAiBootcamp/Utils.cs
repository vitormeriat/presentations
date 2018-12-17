using CNTK;
using System;
using System.Collections.Generic;
using System.Linq;

namespace GlobalAiBootcamp
{
    public static class Utils
    {
        static float[][] mData = new float[][] {
            new float[] { 5.1f, 3.5f, 1.4f, 0.2f},
            new float[] { 4.9f, 3.0f, 1.4f, 0.2f},
            new float[] { 4.7f, 3.2f, 1.3f, 0.2f},
            new float[] { 4.6f, 3.1f, 1.5f, 0.2f},
            new float[] { 6.9f, 3.1f, 4.9f, 1.5f},
            new float[] { 5.5f, 2.3f, 4.0f, 1.3f},
            new float[] { 6.5f, 2.8f, 4.6f, 1.5f},
            new float[] { 5.0f, 3.4f, 1.5f, 0.2f},
            new float[] { 4.4f, 2.9f, 1.4f, 0.2f},
            new float[] { 4.9f, 3.1f, 1.5f, 0.1f},
            new float[] { 5.4f, 3.7f, 1.5f, 0.2f},
            new float[] { 4.8f, 3.4f, 1.6f, 0.2f},
            new float[] { 4.8f, 3.0f, 1.4f, 0.1f},
            new float[] { 4.3f, 3.0f, 1.1f, 0.1f},
            new float[] { 6.5f, 3.0f, 5.8f, 2.2f},
            new float[] { 7.6f, 3.0f, 6.6f, 2.1f},
            new float[] { 4.9f, 2.5f, 4.5f, 1.7f},
            new float[] { 7.3f, 2.9f, 6.3f, 1.8f},
            new float[] { 5.7f, 3.8f, 1.7f, 0.3f},
            new float[] { 5.1f, 3.8f, 1.5f, 0.3f},
        };

        public static void PrintCNTKVersion()
        {
            var version = System.Reflection.Assembly.GetAssembly(typeof(CNTK.Trainer)).FullName;

            var cpu = DeviceDescriptor.UseDefaultDevice();

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"\t{version}");
            Console.WriteLine($"\tHello from CNTK for {cpu.Type}!");
            Console.ResetColor();
        }

        /// <summary>
        /// Normalização de Gauss, calculado o valor médio e o desvio padrão...
        /// </summary>
        public static void Normalization()
        {
            // Define o device onde o cálculo será executado
            var device = DeviceDescriptor.UseDefaultDevice();

            // Exibe os dataset que vai ser normalizado
            Console.WriteLine($"\nX1,\tX2,\tX3,\tX4");
            Console.WriteLine($"-----,\t-----,\t-----,\t-----");
            foreach (var row in mData)
            {
                Console.WriteLine($"{row[0]},\t{row[1]},\t{row[2]},\t{row[3]}");
            }
            Console.WriteLine($"-----,\t-----,\t-----,\t-----\n\n");

            // Converte os dados em um enumerable list
            var data = mData.ToEnumerable<IEnumerable<float>>();

            // Assina os valores 
            var vData = Value.CreateBatchOfSequences<float>(new int[] { 4 }, data, device);

            // Cria uma variável para descrever os dados
            var features = Variable.InputVariable(vData.Shape, DataType.Float);

            // Define a função do CNTK para cálculo da média.
            var mean = CNTKLib.ReduceMean(features, new Axis(2));

            // Realiza o mapeamento entre variáveis e o dado
            var inputDataMap = new Dictionary<Variable, Value>() { { features, vData } };
            var meanDataMap = new Dictionary<Variable, Value>() { { mean, null } };

            // Cálcula a média
            mean.Evaluate(inputDataMap, meanDataMap, device);
            // Obtém o resultado
            var meanValues = meanDataMap[mean].GetDenseData<float>(mean);

            Console.WriteLine($"\nValores médios de cada recurso: x1={meanValues[0][0]},\tx2={meanValues[0][1]},\tx3={meanValues[0][2]},\tx4={meanValues[0][3]}");

            // Cálculo do desvio padrão
            var std = CalculateStd(features);
            var stdDataMap = new Dictionary<Variable, Value>() { { std, null } };
            // Executa o cálculo
            std.Evaluate(inputDataMap, stdDataMap, device);
            // Obtém os resultados
            var stdValues = stdDataMap[std].GetDenseData<float>(std);

            Console.WriteLine($"\nDesvio padrão de cada recurso: x1={stdValues[0][0]},\tx2={stdValues[0][1]},\tx3={stdValues[0][2]},\tx4={stdValues[0][3]}");

            // Assim que tivermos a média e o desvio padrão, podemos calcular os valores normalizados
            var gaussNormalization = CNTKLib.ElementDivide(CNTKLib.Minus(features, mean), std);
            var gaussDataMap = new Dictionary<Variable, Value>() { { gaussNormalization, null } };
            // Executa o cálculo
            gaussNormalization.Evaluate(inputDataMap, gaussDataMap, device);
            // Obtém os resultados
            var normValues = gaussDataMap[gaussNormalization].GetDenseData<float>(gaussNormalization);
            
            // Exibe os valores normalizados
            Console.WriteLine($"\n-------------------------------------------");
            Console.WriteLine($"Valores normalizados para o conjunto de dados\n");
            Console.WriteLine($"X1,\tX2,\tX3,\tX4");
            Console.WriteLine($"-----,\t-----,\t-----,\t-----");
            var row2 = normValues[0];
            for (var j = 0; j < 80; j += 4)
            {
                Console.WriteLine($"{row2[j]},\t{row2[j + 1]},\t{row2[j + 2]},\t{row2[j + 3]}");
            }
            Console.WriteLine($"\nDone!!!");
        }

        private static Function CalculateStd(Variable features)
        {
            var mean = CNTKLib.ReduceMean(features, new Axis(2));
            var remainder = CNTKLib.Minus(features, mean);
            var squared = CNTKLib.Square(remainder);
            var n = new Constant(new NDShape(0), DataType.Float, features.Shape.Dimensions.Last() - 1);
            var elm = CNTKLib.ElementDivide(squared, n);
            var sum = CNTKLib.ReduceSum(elm, new Axis(2));
            var stdVal = CNTKLib.Sqrt(sum);
            return stdVal;
        }

    }

    public static class ArrayExtensions
    {
        public static IEnumerable<T> ToEnumerable<T>(this Array target)
        {
            foreach (var item in target)
                yield return (T)item;
        }
    }
}
