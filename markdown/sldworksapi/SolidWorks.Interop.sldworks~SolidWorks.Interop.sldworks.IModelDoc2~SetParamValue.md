---
title: "SetParamValue Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetParamValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetParamValue.html"
---

# SetParamValue Method (IModelDoc2)

Sets the value of selected dimension (or parameter).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetParamValue( _
   ByVal Val As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Val As System.Double

instance.SetParamValue(Val)
```

### C#

```csharp
void SetParamValue(
   System.double Val
)
```

### C++/CLI

```cpp
void SetParamValue(
   System.double Val
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`: Value of parameter (dimension) in meters or radians

## VBA Syntax

See [ModelDoc2::SetParamValue](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetParamValue.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::Parameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Parameter.html)
[IModelDoc2::IParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IParameter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
