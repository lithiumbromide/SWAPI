---
title: "IsAdvancedMate Property (IDistanceMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDistanceMateFeatureData"
member: "IsAdvancedMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate.html"
---

# IsAdvancedMate Property (IDistanceMateFeatureData)

Gets or sets whether this distance mate is a limit distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsAdvancedMate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDistanceMateFeatureData
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

True if a limit distance mate, false if a standard distance mate

## VBA Syntax

See [DistanceMateFeatureData::IsAdvancedMate](ms-its:sldworksapivb6.chm::/sldworks~DistanceMateFeatureData~IsAdvancedMate.html).

## See Also

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html)
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
