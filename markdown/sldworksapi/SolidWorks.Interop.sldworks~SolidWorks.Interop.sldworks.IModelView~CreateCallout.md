---
title: "CreateCallout Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "CreateCallout"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~CreateCallout.html"
---

# CreateCallout Method (IModelView)

Creates a callout on this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCallout( _
   ByVal NumberOfRows As System.Integer, _
   ByVal LpHandler As System.Object _
) As Callout
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim NumberOfRows As System.Integer
Dim LpHandler As System.Object
Dim value As Callout

value = instance.CreateCallout(NumberOfRows, LpHandler)
```

### C#

```csharp
Callout CreateCallout(
   System.int NumberOfRows,
   System.object LpHandler
)
```

### C++/CLI

```cpp
Callout^ CreateCallout(
   System.int NumberOfRows,
   System.Object^ LpHandler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfRows`: Number of rows in the callout
- `LpHandler`: Pointer to [ISwCalloutHandler](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwCalloutHandler.html)

### Return Value

An [ICallout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) object

## VBA Syntax

See [ModelView::CreateCallout](ms-its:sldworksapivb6.chm::/sldworks~ModelView~CreateCallout.html).

## Examples

[Create a Callout in a Model View (VBA)](Create_Model_View_Callouts_Example_VB.htm)
[Create a Callout in a Model View (VB.NET)](Create_Model_View_Callouts_Example_VBNET.htm)
[Create a Callout in a Model View (C#)](Create_Model_View_Callouts_Example_CSharp.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
