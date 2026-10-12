---
title: "SetSelections Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "SetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections.html"
---

# SetSelections Method (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::SetSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~SetSelections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSelections( _
   ByVal Objects As System.Object, _
   ByVal SelMarks As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim SelMarks As System.Object

instance.SetSelections(Objects, SelMarks)
```

### C#

```csharp
void SetSelections(
   System.object Objects,
   System.object SelMarks
)
```

### C++/CLI

```cpp
void SetSelections(
   System.Object^ Objects,
   System.Object^ SelMarks
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Objects`:
- `SelMarks`:

## VBA Syntax

See [MacroFeatureData::SetSelections](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~SetSelections.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
