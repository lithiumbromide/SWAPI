---
title: "IGetSelections2 Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetSelections2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections2.html"
---

# IGetSelections2 Method (IMacroFeatureData)

Obsolete. Superseded by [IMacroFeatureData::IGetSelections3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetSelections3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetSelections2( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Integer, _
   ByRef SelMarks As System.Integer, _
   ByRef DrViews As View _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim ObjectTypes As System.Integer
Dim SelMarks As System.Integer
Dim DrViews As View

instance.IGetSelections2(SelCount, Objects, ObjectTypes, SelMarks, DrViews)
```

### C#

```csharp
void IGetSelections2(
   System.int SelCount,
   out System.object Objects,
   out System.int ObjectTypes,
   out System.int SelMarks,
   out View DrViews
)
```

### C++/CLI

```cpp
void IGetSelections2(
   System.int SelCount,
   [Out] System.Object^ Objects,
   [Out] System.int ObjectTypes,
   [Out] System.int SelMarks,
   [Out] View^ DrViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelCount`:
- `Objects`:
- `ObjectTypes`:
- `SelMarks`:
- `DrViews`:

## VBA Syntax

See [MacroFeatureData::IGetSelections2](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~IGetSelections2.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
