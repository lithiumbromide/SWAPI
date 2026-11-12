---
title: "ActiveView Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ActiveView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html"
---

# ActiveView Property (IModelDoc2)

Gets the current active model view in read-only mode.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActiveView As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

instance.ActiveView = value

value = instance.ActiveView
```

### C#

```csharp
System.object ActiveView {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ActiveView {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Current active [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) in this document

## VBA Syntax

See [ModelDoc2::ActiveView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ActiveView.html).

## Examples

[Change Wrap Feature (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)
[Get Display State (VBA)](Get_Display_State_Example_VB.htm)
[Set Model Display (VBA)](Set_Model_Display_Mode_Example_VB.htm)
[Create Hidden Undo Object (VBA)](Create_Multiple_Undo_Command_Example_VB.htm)
[Create Hidden Undo Object (VB.NET)](Create_Multiple_Undo_Command_Example_VBNET.htm)
[Create Hidden Undo Object (C#)](Create_Multiple_Undo_Command_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html)
[IModelDoc2::EnumModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.html)
[IModelView::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
