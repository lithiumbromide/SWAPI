---
title: "IsAdvancedMate Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "IsAdvancedMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~IsAdvancedMate.html"
---

# IsAdvancedMate Property (IAngleMateFeatureData)

Gets or sets whether this angle mate is a limit angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsAdvancedMate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
Dim value As System.Boolean

instance.IsAdvancedMate = value

value = instance.IsAdvancedMate
```

### C#

```csharp
System.bool IsAdvancedMate {get; set;}
```

### C++/CLI

```cpp
property System.bool IsAdvancedMate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if a limit angle mate, false if a standard angle mate

## VBA Syntax

See [AngleMateFeatureData::IsAdvancedMate](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~IsAdvancedMate.html).

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
