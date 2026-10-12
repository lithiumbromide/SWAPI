---
title: "InsertSheetMetal3dBend Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertSheetMetal3dBend"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertSheetMetal3dBend.html"
---

# InsertSheetMetal3dBend Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertSheetMetal3dBend](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSheetMetal3dBend.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSheetMetal3dBend( _
   ByVal Angle As System.Double, _
   ByVal Radius As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal BendPos As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Angle As System.Double
Dim Radius As System.Double
Dim FlipDir As System.Boolean
Dim BendPos As System.Short

instance.InsertSheetMetal3dBend(Angle, Radius, FlipDir, BendPos)
```

### C#

```csharp
void InsertSheetMetal3dBend(
   System.double Angle,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos
)
```

### C++/CLI

```cpp
void InsertSheetMetal3dBend(
   System.double Angle,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `Radius`:
- `FlipDir`:
- `BendPos`:

## VBA Syntax

See [ModelDoc::InsertSheetMetal3dBend](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertSheetMetal3dBend.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
