---
title: "CreateEllipticalArcByCenter Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateEllipticalArcByCenter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateEllipticalArcByCenter.html"
---

# CreateEllipticalArcByCenter Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateEllipticalArcByCenter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEllipticalArcByCenter( _
   ByVal Center As System.Object, _
   ByVal Major As System.Object, _
   ByVal Minor As System.Object, _
   ByVal Start As System.Object, _
   ByVal End As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Center As System.Object
Dim Major As System.Object
Dim Minor As System.Object
Dim Start As System.Object
Dim End As System.Object
Dim value As System.Boolean

value = instance.CreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

### C#

```csharp
System.bool CreateEllipticalArcByCenter(
   System.object Center,
   System.object Major,
   System.object Minor,
   System.object Start,
   System.object End
)
```

### C++/CLI

```cpp
System.bool CreateEllipticalArcByCenter(
   System.Object^ Center,
   System.Object^ Major,
   System.Object^ Minor,
   System.Object^ Start,
   System.Object^ End
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Major`:
- `Minor`:
- `Start`:
- `End`:

## VBA Syntax

See [ModelDoc::CreateEllipticalArcByCenter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateEllipticalArcByCenter.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
