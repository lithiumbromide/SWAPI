---
title: "ISetSelections Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "ISetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections.html"
---

# ISetSelections Method (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::ISetSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~ISetSelections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSelections( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef SelMarks As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim SelMarks As System.Integer

instance.ISetSelections(SelCount, Objects, SelMarks)
```

### C#

```csharp
void ISetSelections(
   System.int SelCount,
   ref System.object Objects,
   ref System.int SelMarks
)
```

### C++/CLI

```cpp
void ISetSelections(
   System.int SelCount,
   System.Object^% Objects,
   System.int% SelMarks
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelCount`:
- `Objects`:
- `SelMarks`:

## VBA Syntax

See [MacroFeatureData::ISetSelections](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~ISetSelections.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
