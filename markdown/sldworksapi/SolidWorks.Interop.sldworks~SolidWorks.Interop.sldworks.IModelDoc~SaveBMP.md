---
title: "SaveBMP Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SaveBMP"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveBMP.html"
---

# SaveBMP Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SaveBMP](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SaveBMP.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveBMP( _
   ByVal FileNameIn As System.String, _
   ByVal WidthIn As System.Integer, _
   ByVal HeightIn As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FileNameIn As System.String
Dim WidthIn As System.Integer
Dim HeightIn As System.Integer
Dim value As System.Boolean

value = instance.SaveBMP(FileNameIn, WidthIn, HeightIn)
```

### C#

```csharp
System.bool SaveBMP(
   System.string FileNameIn,
   System.int WidthIn,
   System.int HeightIn
)
```

### C++/CLI

```cpp
System.bool SaveBMP(
   System.String^ FileNameIn,
   System.int WidthIn,
   System.int HeightIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileNameIn`:
- `WidthIn`:
- `HeightIn`:

## VBA Syntax

See [ModelDoc::SaveBMP](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SaveBMP.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
