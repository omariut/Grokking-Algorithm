# products = {}
# products["water"] = {}
# products["book"] = {}
# products["food"] = {}
# products["jacket"] = {}
# products["camera"] = {}

# products["water"]["weight"] = 3
# products["book"]["weight"] = 1
# products["food"]["weight"] = 2
# products["jacket"]["weight"] = 2
# products["camera"]["weight"] = 1

# products["water"]["value"] = 10
# products["book"]["value"] = 3
# products["food"]["value"] = 9
# products["jacket"]["value"] = 5
# products["camera"]["value"] = 6

products = {}
products["g"] = {}
products["s"] = {}
products["laptop"] = {}
products["iphone"] = {}
products["g"] ["weight"]= 1
products["s"] ["weight"]= 4
products["laptop"]["weight"] = 3
products["iphone"] ["weight"]= 1
products["g"] ["value"]= 1500
products["s"] ["value"]= 3000
products["laptop"]["value"] = 2000
products["iphone"] ["value"]= 2000
sack_weight = 4
row = len(products)
final_products = []
new_total_wt = 0
i = 1

min_wt = min([value["weight"] for key, value in products.items()])
c = [[0 for i in range (row +1 )] for j in range (sack_weight +1)]
p = [["" for i in range (row  +1 )] for j in range (sack_weight +1)]
for key, value in products.items():
    for j in range(1,sack_weight+1, min_wt):
        rm_wt = j - value["weight"]
        if rm_wt >= 0 and c[i-1][j] <=  value["value"] + c[i-1][rm_wt]:
            c[i][j] = value["value"] + c[i-1][rm_wt]
            p[i][j] = key + " "  +  p[i-1][rm_wt] 
            
        else :
            c[i][j] = c[i-1][j]
            p[i][j] = p[i-1][j]
        
    
    
    print(c[i])
    print(p[row ][sack_weight])
    i+=1







    