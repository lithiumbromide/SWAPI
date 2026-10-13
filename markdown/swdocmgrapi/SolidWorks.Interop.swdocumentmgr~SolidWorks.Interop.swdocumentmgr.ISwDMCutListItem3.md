---
title: "ISwDMCutListItem3 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem3"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3.html"
---

# ISwDMCutListItem3 Interface

Accesses cut-list items.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMCutListItem3
   Inherits ISwDMCutListItem, ISwDMCutListItem2
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem3
```

### C#

```csharp
public interface ISwDMCutListItem3 : ISwDMCutListItem, ISwDMCutListItem2
```

### C++/CLI

```cpp
public interface class ISwDMCutListItem3 : public ISwDMCutListItem, ISwDMCutListItem2
```

## VBA Syntax

See [SwDMCutListItem3](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem3.html).

## Remarks

- You can access an ISwCutListItem3 object by calling QueryInterface on an [ISwDMCutListItem](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMCutListItem.html) object in C++ or by direct assignment in Visual Basic.
- The ISwDMCutListItem object can be assigned to an ISwDMCutListItem3 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMConfiguration16::GetCutListItems](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration16~GetCutListItems.html)

[ISwDMDocument10::GetCutListItems2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument13~GetCutListItems2.html)

## See Also

[ISwDMCutListItem3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem3_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMCutListItem Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem.html)
[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.html)
