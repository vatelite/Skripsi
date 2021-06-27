def findDecision(obj): #obj[0]: Qmc, obj[1]: Qhv, obj[2]: Qlv, obj[3]: Qmv
   # {"feature": "Qmv", "instances": 126, "metric_value": 1.9998, "depth": 1}
   if obj[3]>0.21472883258507253:
      # {"feature": "Qlv", "instances": 95, "metric_value": 1.5848, "depth": 2}
      if obj[2]>0.6915819963894737:
         # {"feature": "Qhv", "instances": 57, "metric_value": 0.9944, "depth": 3}
         if obj[1]>0.3608074133516814:
            # {"feature": "Qmc", "instances": 51, "metric_value": 0.9662, "depth": 4}
            if obj[0]>0.5400761066266792:
               return 'D'
            elif obj[0]<=0.5400761066266792:
               return 'C'
            else:
               return 'C'
         elif obj[1]<=0.3608074133516814:
            return 'C'
         else:
            return 'C'
      elif obj[2]<=0.6915819963894737:
         # {"feature": "Qmc", "instances": 38, "metric_value": 0.6292, "depth": 3}
         if obj[0]<=0.6503436066287539:
            # {"feature": "Qhv", "instances": 30, "metric_value": 0.2108, "depth": 4}
            if obj[1]<=0.2573734000999999:
               return 'B'
            elif obj[1]>0.2573734000999999:
               return 'B'
            else:
               return 'B'
         elif obj[0]>0.6503436066287539:
            # {"feature": "Qhv", "instances": 8, "metric_value": 0.9544, "depth": 4}
            if obj[1]>0.425709516:
               return 'C'
            elif obj[1]<=0.425709516:
               return 'B'
            else:
               return 'B'
         else:
            return 'C'
      else:
         return 'B'
   elif obj[3]<=0.21472883258507253:
      return 'A'
   else:
      return 'A'
