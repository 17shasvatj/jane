import json
import requests
import subprocess
def push(jString):
    product_dict = json.loads(jString)
    prop = product_dict['properties']
    #cid = find('$device_id', prop, 'cid')
    uid = find('$user_id', prop, 'cid')+'&'
    cid=find('$device_id', prop, 'cid')+'&'
    ec = 'ec=UX&'
    ea='ea=click&'
    prnm = find('productName', prop, 'pr1nm')+'&'
    prbr = find('productBrand', prop, 'pr1br')+'&'
    prca = find('productKind', prop, 'pr1ca')+'&'
    prva = find('productLineage', prop, 'pr1va')
    prid = find('productId', prop, 'pr1id')
    t='t=event'+'&'
    v1 = 'v=1'+'&'
    dl = find('og_ref', prop, 'dl')+'&'
    tid = 'tid=UA-168927380-1'+'&'
    pa1 = 'pa=add&'
    pal = 'pal=List&'
    ua='ua=user-agent&'
    postStr = 'curl -d "' + ua+ v1+t+tid+cid+uid+ec+ea+pal+pa1+prid+prnm+prbr+prca+prva +  '" -X POST https://www.google-analytics.com/collect'
    p = subprocess.Popen(postStr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(out)
    print(err)
    print(postStr)
    
    
    
    
    

def find(param, dict, anParam):
    if(param in dict.keys()):
        val = anParam +"="+dict[param]
        val = val.replace(" ", "%20")
        return val
    else:
        return ""
    


jso = '{"event": "Viewed Product", "properties": {"time": 1591115353, "$browser": "Chrome", "$browser_version": 83, "$device": "Android", "$device_id": "1720b7bae935-0177a139c71c26-270e1c5d-38400-1720b7bae94d", "$insert_id": "gvsvdfghnepsu786", "$lib_version": "2.37.0", "$os": "Android", "$region": "Illinois", "$screen_height": 640, "$screen_width": 360, "$user_id": "123284", "Test: Fee Label": "pinkFreeSymbol", "Test: Login": "new", "Test: Pdp Cta": "old", "Test: Product Reviews": "off", "Test: Stores Map": "off", "app": "embed", "appStoreId": "1687", "build": "450216e", "mp_country_code": "US", "mp_lib": "web", "mp_procesing_time_ms": 1591140690532, "og_ref": "https://www.foo.com/order-now", "productAggregateRating": 4.05, "productBrand": "Verano", "productId": "153539", "productKind": "flower", "productLineage": "hybrid", "productName": "Sonny G", "productReviewCount": 20, "productReviewsVisible": false, "recommended": false, "storeCity": "Marion", "storeState": "Illinois"}}'
jso = jso.replace("'", '"')
push(jso)