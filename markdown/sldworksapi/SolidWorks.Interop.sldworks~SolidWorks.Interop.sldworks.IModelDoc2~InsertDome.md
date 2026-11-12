---
title: "InsertDome Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertDome"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDome.html"
---

# InsertDome Method (IModelDoc2)

Inserts a dome.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertDome( _
   ByVal Height As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal DoEllipticSurface As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Height As System.Double
Dim ReverseDir As System.Boolean
Dim DoEllipticSurface As System.Boolean

instance.InsertDome(Height, ReverseDir, DoEllipticSurface)
```

### C#

```csharp
void InsertDome(
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
)
```

### C++/CLI

```cpp
void InsertDome(
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Height`: Height for the dome in meters
- `ReverseDir`: True if you want to reverse the dome direction, false if not
- `DoEllipticSurface`: RUE if you want the dome to be an elliptical surface, false if not

## VBA Syntax

See [ModelDoc2::InsertDome](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertDome.html).

## Examples

[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

## Remarks

Before using this method, you must select the face for the dome using a selection mark of 1. See [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
