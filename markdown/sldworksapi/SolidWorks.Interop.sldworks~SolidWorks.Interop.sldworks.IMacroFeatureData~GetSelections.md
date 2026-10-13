---
title: "GetSelections Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections.html"
---

# GetSelections Method (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::GetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSelections( _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Object, _
   ByRef SelMarks As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim ObjectTypes As System.Object
Dim SelMarks As System.Object

instance.GetSelections(Objects, ObjectTypes, SelMarks)
```

### C#

```csharp
void GetSelections(
   out System.object Objects,
   out System.object ObjectTypes,
   out System.object SelMarks
)
```

### C++/CLI

```cpp
void GetSelections(
   [Out] System.Object^ Objects,
   [Out] System.Object^ ObjectTypes,
   [Out] System.Object^ SelMarks
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Objects`:
- `ObjectTypes`:
- `SelMarks`:

## VBA Syntax

See [MacroFeatureData::GetSelections](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetSelections.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
