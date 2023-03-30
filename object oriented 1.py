class TvModel:
      def tv_fun(self,model,operation):
          print("Model:",model)
          print("operation:",operation)

class FridgeModel:
      def fridge_fun(self,model,operation):
          print("Model:",model)
          print("opration:",operation)

tv1=TvModel()
fd1=FridgeModel()
tv1.tv_fun("sony","vidio")
fd1.fridge_fun("BPL","cooling")
tv1.fridge_fun()
fd1.tv_fun()
