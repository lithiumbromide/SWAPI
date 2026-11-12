---
title: "InsertBkgImage Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertBkgImage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html"
---

# InsertBkgImage Method (IModelDoc2)

Inserts the scene background image.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertBkgImage( _
   ByVal NewName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NewName As System.String

instance.InsertBkgImage(NewName)
```

### C#

```csharp
void InsertBkgImage(
   System.string NewName
)
```

### C++/CLI

```cpp
void InsertBkgImage(
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewName`: Path to image file including file extension

## VBA Syntax

See [ModelDoc2::InsertBkgImage](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertBkgImage.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::DeleteBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBkgImage.html)
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.html)
[IModelDoc2::SceneBkgImageFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.html)
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.html)
[IModelDocExtension::SetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.html)
[IModelDocExtension::GetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
