---
title: "IGetSelections Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections.html"
---

# IGetSelections Method (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::IGetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetSelections( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Integer, _
   ByRef SelMarks As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim ObjectTypes As System.Integer
Dim SelMarks As System.Integer

instance.IGetSelections(SelCount, Objects, ObjectTypes, SelMarks)
```

### C#

```csharp
void IGetSelections(
   System.int SelCount,
   out System.object Objects,
   out System.int ObjectTypes,
   out System.int SelMarks
)
```

### C++/CLI

```cpp
void IGetSelections(
   System.int SelCount,
   [Out] System.Object^ Objects,
   [Out] System.int ObjectTypes,
   [Out] System.int SelMarks
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelCount`:
- `Objects`:
- `ObjectTypes`:
- `SelMarks`:

## VBA Syntax

See [MacroFeatureData::IGetSelections](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~IGetSelections.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
