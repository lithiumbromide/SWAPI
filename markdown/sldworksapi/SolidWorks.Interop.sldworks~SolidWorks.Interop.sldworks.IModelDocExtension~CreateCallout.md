---
title: "CreateCallout Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateCallout"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateCallout.html"
---

# CreateCallout Method (IModelDocExtension)

Creates a callout independent of a selection.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCallout( _
   ByVal NumberOfRows As System.Integer, _
   ByVal Handler As System.Object _
) As Callout
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NumberOfRows As System.Integer
Dim Handler As System.Object
Dim value As Callout

value = instance.CreateCallout(NumberOfRows, Handler)
```

### C#

```csharp
Callout CreateCallout(
   System.int NumberOfRows,
   System.object Handler
)
```

### C++/CLI

```cpp
Callout^ CreateCallout(
   System.int NumberOfRows,
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfRows`: Number of rows in the callout
- `Handler`: Pointer to the event handler for the callout ([ISwCalloutHandler](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.html))

### Return Value

[Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html)

## VBA Syntax

See [ModelDocExtension::CreateCallout](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateCallout.html).

## Examples

[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)
[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)

## Remarks

This method allows you to create a callout independently of a selection. You can define the position of the callout using the [ICallout::Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout~Position.html) and [ICallout::SetTargetPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout~SetTargetPoint.html).

To create a callout dependent on a selection, use [ISelectionMgr::CreateCallout2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~CreateCallout2.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
