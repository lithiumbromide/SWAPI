---
title: "IPropertyManagerPageWindowFromHandle Interface"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageWindowFromHandle"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html"
---

# IPropertyManagerPageWindowFromHandle Interface

Allows you to access a [PropertyManager page](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html) .NET control.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPropertyManagerPageWindowFromHandle
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageWindowFromHandle
```

### C#

```csharp
public interface IPropertyManagerPageWindowFromHandle
```

### C++/CLI

```cpp
public interface class IPropertyManagerPageWindowFromHandle
```

## VBA Syntax

See [PropertyManagerPageWindowFromHandle](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageWindowFromHandle.html).

## Examples

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

## Remarks

The add-in that deploys a .NET control in a PropertyManager page must implement the event handler [IPropertyManagerPage2Handler8::OnWindowFromHandleControlCreated](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnWindowFromHandleControlCreated.html). SOLIDWORKS populates the arguments of this handler when it attempts to create a .NET control on the PropertyManager page.

If SOLIDWORKS is unable to create a .NET control, it passes Status = false in the handler. When Status = false, the handler must return an action to take as defined in [swHandleWindowFromHandleCreationFailure_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHandleWindowFromHandleCreationFailure_e.html).

See [Using PropertyManagerPage2 and the Related Objects](sldworksapiprogguide.chm::/overview/Using_PropertyManagerPage2_and_the_Related_Objects.htm) for more information.

## Accessors

[IPropertyManagerPage2::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) and [IPropertyManagerPage2::IAddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html)

## Access Diagram

[PropertyManagerPageWindowFromHandle](SWObjectModel.pdf#PropertyManagerPageWindowFromHa)

## See Also

[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
