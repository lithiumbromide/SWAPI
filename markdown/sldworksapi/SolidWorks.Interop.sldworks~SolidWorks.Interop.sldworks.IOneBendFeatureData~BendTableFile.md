---
title: "BendTableFile Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "BendTableFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendTableFile.html"
---

# BendTableFile Property (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html) and [IOneBendFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendTableFile As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
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

See [OneBendFeatureData::BendTableFile](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~BendTableFile.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
