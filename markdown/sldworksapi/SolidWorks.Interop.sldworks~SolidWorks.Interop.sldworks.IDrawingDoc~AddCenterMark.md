---
title: "AddCenterMark Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AddCenterMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddCenterMark.html"
---

# AddCenterMark Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertCenterMark2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertCenterMark2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCenterMark( _
   ByVal CmSize As System.Double, _
   ByVal CmShowLines As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim CmSize As System.Double
Dim CmShowLines As System.Boolean
Dim value As System.Boolean

value = instance.AddCenterMark(CmSize, CmShowLines)
```

### C#

```csharp
System.bool AddCenterMark(
   System.double CmSize,
   System.bool CmShowLines
)
```

### C++/CLI

```cpp
System.bool AddCenterMark(
   System.double CmSize,
   System.bool CmShowLines
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CmSize`:
- `CmShowLines`:

## VBA Syntax

See [DrawingDoc::AddCenterMark](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AddCenterMark.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
