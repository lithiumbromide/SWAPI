---
title: "GetVectorVB Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "GetVectorVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVectorVB.html"
---

# GetVectorVB Method (IParameter)

Extracts information of type vector from a parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVectorVB() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim value As System.Object

value = instance.GetVectorVB()
```

### C#

```csharp
System.object GetVectorVB()
```

### C++/CLI

```cpp
System.Object^ GetVectorVB();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 3 values in the vector (see **Remarks**)

## VBA Syntax

See [Parameter::GetVectorVB](ms-its:sldworksapivb6.chm::/sldworks~Parameter~GetVectorVB.html).

## Remarks

This method packs the data into a SafeArray in Visual Basic for Applications (VBA):

[ X,Y,Z ]

where:

| (double) X | x vector value stored on the parameter |
| --- | --- |
| (double) Y | y vector value stored on the parameter |
| (double) Z | z vector value stored on the parameter |

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
[IParameter::GetVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVector.html)
[IParameter::SetVector2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
