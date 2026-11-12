---
title: "EditBody Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "EditBody"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBody.html"
---

# EditBody Property (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::IGetEditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetEditBodies.html), [IMacroFeatureData::ISetEditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~ISetEditBodies.html), and [IMacroFeatureData::EditBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~EditBodies.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EditBody As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As Body2

instance.EditBody = value

value = instance.EditBody
```

### C#

```csharp
Body2 EditBody {get; set;}
```

### C++/CLI

```cpp
property Body2^ EditBody {
   Body2^ get();
   void set (    Body2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [MacroFeatureData::EditBody](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~EditBody.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
