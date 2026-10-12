---
title: "EnableDraft Property (IRibFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData"
member: "EnableDraft"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData~EnableDraft.html"
---

# EnableDraft Property (IRibFeatureData)

Obsolete. Superseded by [IRibFeatureData2::EnableDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~EnableDraft.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableDraft As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData
Dim value As System.Boolean

instance.EnableDraft = value

value = instance.EnableDraft
```

### C#

```csharp
System.bool EnableDraft {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableDraft {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RibFeatureData::EnableDraft](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData~EnableDraft.html).

## See Also

[IRibFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData.html)
[IRibFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData_members.html)
