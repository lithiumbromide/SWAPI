---
title: "KeepBodies Property (IDeleteBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteBodyFeatureData"
member: "KeepBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~KeepBodies.html"
---

# KeepBodies Property (IDeleteBodyFeatureData)

Gets or sets whether to keep bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteBodyFeatureData
Dim value As System.Boolean

instance.KeepBodies = value

value = instance.KeepBodies
```

### C#

```csharp
System.bool KeepBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep bodies, false to delete bodies

## VBA Syntax

See [DeleteBodyFeatureData::KeepBodies](ms-its:sldworksapivb6.chm::/sldworks~DeleteBodyFeatureData~KeepBodies.html).

## Examples

See the [IDeleteBodyFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData.html) examples.

## Remarks

Call [IDeleteBodyFeatureData::Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData~Bodies.html) to specify the bodies to keep or delete.

## See Also

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
