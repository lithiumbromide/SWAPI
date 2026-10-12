---
title: "BendTableFile Property (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "BendTableFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~BendTableFile.html"
---

# BendTableFile Property (IBendsFeatureData)

Obsolete. Superseded by [IBendsFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html) and [IBendsFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendTableFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
Dim value As System.String

instance.BendTableFile = value

value = instance.BendTableFile
```

### C#

```csharp
System.string BendTableFile {get; set;}
```

### C++/CLI

```cpp
property System.String^ BendTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [BendsFeatureData::BendTableFile](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~BendTableFile.html).

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
