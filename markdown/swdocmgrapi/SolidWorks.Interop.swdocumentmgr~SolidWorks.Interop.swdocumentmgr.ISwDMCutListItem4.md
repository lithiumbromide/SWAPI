---
title: "ISwDMCutListItem4 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem4"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.html"
---

# ISwDMCutListItem4 Interface

Accesses cut-list items.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMCutListItem4
   Inherits ISwDMCutListItem, ISwDMCutListItem2, ISwDMCutListItem3
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem4
```

### C#

```csharp
public interface ISwDMCutListItem4 : ISwDMCutListItem, ISwDMCutListItem2, ISwDMCutListItem3
```

### C++/CLI

```cpp
public interface class ISwDMCutListItem4 : public ISwDMCutListItem, ISwDMCutListItem2, ISwDMCutListItem3
```

## VBA Syntax

See [SwDMCutListItem4](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem4.html).

## Remarks

- You can access an ISwCutListItem4 object by calling QueryInterface on an [ISwDMCutListItem](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMCutListItem.html) object in C++ or by direct assignment in Visual Basic.
- The ISwDMCutListItem object can be assigned to an ISwDMCutListItem4 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMConfiguration16::GetCutListItems](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration16~GetCutListItems.html)

[ISwDMDocument10::GetCutListItems2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument13~GetCutListItems2.html)

## See Also

[ISwDMCutListItem4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.html)
[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3.html)
