---
title: "GetSelections2 Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetSelections2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections2.html"
---

# GetSelections2 Method (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::GetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetSelections3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSelections2( _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Object, _
   ByRef SelMarks As System.Object, _
   ByRef DrViews As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim ObjectTypes As System.Object
Dim SelMarks As System.Object
Dim DrViews As System.Object

instance.GetSelections2(Objects, ObjectTypes, SelMarks, DrViews)
```

### C#

```csharp
void GetSelections2(
   out System.object Objects,
   out System.object ObjectTypes,
   out System.object SelMarks,
   out System.object DrViews
)
```

### C++/CLI

```cpp
void GetSelections2(
   [Out] System.Object^ Objects,
   [Out] System.Object^ ObjectTypes,
   [Out] System.Object^ SelMarks,
   [Out] System.Object^ DrViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Objects`:
- `ObjectTypes`:
- `SelMarks`:
- `DrViews`:

## VBA Syntax

See [MacroFeatureData::GetSelections2](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetSelections2.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
