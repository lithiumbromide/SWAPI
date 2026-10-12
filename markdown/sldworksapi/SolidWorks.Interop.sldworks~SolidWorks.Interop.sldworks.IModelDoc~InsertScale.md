---
title: "InsertScale Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertScale.html"
---

# InsertScale Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertScale.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertScale( _
   ByVal ScaleFactor_x As System.Double, _
   ByVal ScaleFactor_y As System.Double, _
   ByVal ScaleFactor_z As System.Double, _
   ByVal IsUniform As System.Boolean, _
   ByVal ScaleType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ScaleFactor_x As System.Double
Dim ScaleFactor_y As System.Double
Dim ScaleFactor_z As System.Double
Dim IsUniform As System.Boolean
Dim ScaleType As System.Integer

instance.InsertScale(ScaleFactor_x, ScaleFactor_y, ScaleFactor_z, IsUniform, ScaleType)
```

### C#

```csharp
void InsertScale(
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType
)
```

### C++/CLI

```cpp
void InsertScale(
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ScaleFactor_x`:
- `ScaleFactor_y`:
- `ScaleFactor_z`:
- `IsUniform`:
- `ScaleType`:

## VBA Syntax

See [ModelDoc::InsertScale](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertScale.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
