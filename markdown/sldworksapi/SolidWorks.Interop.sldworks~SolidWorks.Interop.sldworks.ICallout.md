---
title: "ICallout Interface"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html"
---

# ICallout Interface

Allows add-in applications to manipulate single and multi-row callouts.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICallout
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
```

### C#

```csharp
public interface ICallout
```

### C++/CLI

```cpp
public interface class ICallout
```

## VBA Syntax

See [Callout](ms-its:sldworksapivb6.chm::/sldworks~Callout.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

## Remarks

To create callouts, you must implement the [ISwCalloutHandler](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.html) interface.

## Accessors

[IModelDocExtension::CreateCallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateCallout.html) (independent of a selection)

[IModelView::CreateCallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~CreateCallout.html)

[IPropertyManagerPageSelectionbox::Callout Property](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSelectionbox~Callout.html)

[ISelectData::Callout Property](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData~Callout.html)

[ISelectionMgr::CreateCallout2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateCallout2.html) (dependent on a selection)

## Access Diagram

[Callout](SWObjectModel.pdf#Callout)

## See Also

[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
