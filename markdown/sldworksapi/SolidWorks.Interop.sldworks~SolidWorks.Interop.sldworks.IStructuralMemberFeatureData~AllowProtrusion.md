---
title: "AllowProtrusion Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "AllowProtrusion"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~AllowProtrusion.html"
---

# AllowProtrusion Property (IStructuralMemberFeatureData)

Gets or sets whether to allow protrusion.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowProtrusion As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Boolean

instance.AllowProtrusion = value

value = instance.AllowProtrusion
```

### C#

```csharp
System.bool AllowProtrusion {get; set;}
```

### C++/CLI

```cpp
property System.bool AllowProtrusion {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to allow protrusion, false to not

## VBA Syntax

See [StructuralMemberFeatureData::AllowProtrusion](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~AllowProtrusion.html).

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
