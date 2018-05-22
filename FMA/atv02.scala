/*import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.feature.Normalizer
import org.apache.spark.mllib.regression.LinearRegressionWithSGD

val path = "/var/www/html/pos-graduacao/FMA/exemplosml/Atividade2/Dados/lpsa.dat"

val data = sc.textFile(path)

val parsedData = data.map { line =>
val x : Array[String] = line.replace(",", " ").split(" ")
val y = x.map{ (a => a.toDouble)}
val d = y.size - 1
val c = Vectors.dense(y(0),y(d))
LabeledPoint(y(0), c)}.cache()

var numIterarions = 100

val stepSize = 0.00000001;

val model = LinearRegressionWithSGD.train(parsedData, numIterarions, stepSize)

val valuesAndPreds = parsedData.map { point =>
val prediction = model.predict(point.features)
(point.label, prediction)}

valuesAndPreds.take(9).foreach((result) => println(s"predicted label: ${result._1}, actual label: ${result._2}"))

val MSE = valuesAndPreds.map{ case(v, p) => math.pow((v -
p), 2) }.mean()
println("training Mean Squared Error = " + MSE)
*/



import org.apache.spark.mllib.tree.DecisionTree
import org.apache.spark.mllib.tree.model.DecisionTreeModel
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.feature.Normalizer

val path = "/var/www/html/pos-graduacao/FMA/exemplosml/Atividade3/Dados/arvore.txt"

val data = sc.textFile(path).map(
l => l.split("\\s+"))

var dbl = data.map (m => m.map(l => l.toDouble))

val parsedData = dbl.map { y =>
val c = Vectors.dense(y(1),y(2),y(3),y(4),y(5),y(6),y(7))
LabeledPoint(y(0), c)}.cache()

val numClasses = 3

val categoricalFeaturesInfo = Map(6 -> 3)
val impurity = "gini"
val maxDepth = 9
val maxBins = 7

val model = DecisionTree.trainClassifier(parsedData, numClasses,categoricalFeaturesInfo , impurity, maxDepth, maxBins)
println("Learned classification tree model:\n" + model.toDebugString)