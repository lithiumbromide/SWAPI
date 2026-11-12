---
title: "eDApplicationParams Class"
project: ""
interface: "eDApplicationParams"
member: ""
kind: "class"
source: "emodeltoolkit/eDApplicationParams/eDapplicationParams_Class.htm"
---

# eDApplicationParams Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains data that identifies all eDrawings files serialized from your application.

#### Header file code

```vb
class eDApplicationParams
{
public:

ECHAR * ProductName; //Product name

ECHAR * ProductVersion;  //Product version

ECHAR * ProductBuild; //Product build number

ECHAR * LicenseString; //License number

eDApplicationParams()
{ ProductName = ProductVersion = ProductBuild = LicenseString = NULL; }

};
```
