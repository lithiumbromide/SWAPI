---
title: "SceneBkgImageFileName Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SceneBkgImageFileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneBkgImageFileName.html"
---

# SceneBkgImageFileName Property (IModelDoc2)

Controls the image filename used as the current background picture.

## Syntax

### Visual Basic (Declaration)

```vb
Property SceneBkgImageFileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.String

instance.SceneBkgImageFileName = value

value = instance.SceneBkgImageFileName
```

### C#

```csharp
System.string SceneBkgImageFileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ SceneBkgImageFileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the image file

## VBA Syntax

See [ModelDoc2::SceneBkgImageFileName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SceneBkgImageFileName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::DeleteBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBkgImage.html)
[IModelDoc2::InsertBkgImage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html)
[IModelDoc2::GetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneBkgDIB.html)
[IModelDocExtension::GetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSceneBkgDIBx64.html)
[IModelDocExtension::SetSceneBkgDIBx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSceneBkgDIBx64.html)
[IModelDoc2::SetSceneBkgDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSceneBkgDIB.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
