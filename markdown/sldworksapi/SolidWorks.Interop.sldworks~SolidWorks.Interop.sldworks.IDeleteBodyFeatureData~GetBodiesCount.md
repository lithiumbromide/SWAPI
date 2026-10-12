---
title: "GetBodiesCount Method (IDeleteBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteBodyFeatureData"
member: "GetBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount.html"
---

# GetBodiesCount Method (IDeleteBodyFeatureData)

Gets the number of bodies to delete or keep.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteBodyFeatureData
Dim value As System.Integer

value = instance.GetBodiesCount()
```

### C#

```csharp
System.int GetBodiesCount()
```

### C++/CLI

```cpp
System.int GetBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies

## VBA Syntax

See [DeleteBodyFeatureData::GetBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~DeleteBodyFeatureData~GetBodiesCount.html).

## Examples

See the [IDeleteBodyFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData.html) examples.

## Remarks

Call this method before calling [IDeleteBodyFeautre::IGetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.html) to determine the size of the array.

## See Also

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.html)
[IDeleteBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies.html)
[IDeleteBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
