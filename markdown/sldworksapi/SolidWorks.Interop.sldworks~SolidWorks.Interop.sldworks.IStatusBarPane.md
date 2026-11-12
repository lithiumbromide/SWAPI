---
title: "IStatusBarPane Interface"
project: "SOLIDWORKS API Help"
interface: "IStatusBarPane"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.html"
---

# IStatusBarPane Interface

Controls user-created status bar panes in the lower-right corner of the SOLIDWORKS status bar.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IStatusBarPane
```

### Visual Basic (Usage)

```vb
Dim instance As IStatusBarPane
```

### C#

```csharp
public interface IStatusBarPane
```

### C++/CLI

```cpp
public interface class IStatusBarPane
```

## VBA Syntax

See [StatusBarPane](ms-its:sldworksapivb6.chm::/sldworks~StatusBarPane.html).

## Remarks

To use a status bar pane in a project, declare it in your project and manage it during the life cycle of the client application and release just before the client application disconnects from SOLIDWORKS. You can create up to five (5) panes.

## Accessors

[IFrame::GetStatusBarPane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~GetStatusBarPane.html)

## Access Diagram

[StatusBarPane](SWObjectModel.pdf#StatusBarPane)

## See Also

[IStatusBarPane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
