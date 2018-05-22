import org.apache.spark.mllib.clustering.{KMeans, KMeansModel}
import org.apache.spark.mllib.linalg.Vectors
import spark.sqlContext.implicits._
import org.apache.spark.sql.types._

val path = "/var/www/html/pos-graduacao/FMA/exemplosml/TrabalhoPratico/Dados/crime.csv"

val rdd = sc.textFile(path)

def stoDouble (s : String): Double = {return s.map(_.toByte.doubleValue()).reduceLeft( (x,y) => x + y)}

case class StateCode(State:String, Code:Double)
var lines = rdd.map(l => l.split(","))

var states = lines.map(l => StateCode(l(0),stoDouble(l(0)))).toDF()

states.show()
states.createOrReplaceTempView("states")

def makeDouble (s: String): Array[Double] = {
	var str = s.split(",")
	var a = stoDouble(str(0))
	return Array(a,str(2).toDouble,str(3).toDouble,str(4).toDouble,str(5).toDouble)
}

val crime = rdd.map(m => makeDouble(m))

val crimeVector = crime.map(a => Vectors.dense(a(0),a(1),a(2),a(3),a(4)))

//val crime = rdd.map(m => makeDouble(m))

case class Crime(Code:Double, Murder:Double, Assault:Double, UrbanPop:Double, Rape:Double, PredictionVector:org.apache.spark.mllib.linalg.Vector, Prediction:Double)

val clusters = KMeans.train(crimeVector, 5, 10)
val crimeClass = crimeVector.map(a => Crime(a(0), a(1), a(2), a(3), a(4), a ,clusters.predict(a))).toDF()

crimeClass.show()

crimeClass.createOrReplaceTempView("crimes")

//spark.sql("select State, Prediction, UrbanPop, from crimes inner join states on crimes.Code = states.Code order by Prediction Desc").show(50,false)