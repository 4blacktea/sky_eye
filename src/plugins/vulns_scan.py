import requests
import json

```
{
    "CVE-xxxx-xxxx":{
        "fix":{
        
        }
        "poc":{
            "method":"POST",
            "header":{},
            "body":""    
        }
    }
}
```



pocs = json.load("./poc.txt")
for poc in pocs.key:
    if poc[poc]["poc"] == "body":
        req
】






