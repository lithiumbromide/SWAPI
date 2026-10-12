---
title: "DDrawingDocEvents_InsertTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_InsertTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_InsertTableNotifyEventHandler.html"
---

# DDrawingDocEvents_InsertTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your program when a table has been inserted in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_InsertTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.String, _
   ByVal TemplatePath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_InsertTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_InsertTableNotifyEventHandler(
   TableAnnotation TableAnnotation,
   System.string TableType,
   System.string TemplatePath
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_InsertTableNotifyEventHandler(
   TableAnnotation^ TableAnnotation,
   System.String^ TableType,
   System.String^ TemplatePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableAnnotation`: [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)
- `TableType`: Type of table as defined in [swTableAnnotationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)
- `TemplatePath`: Full path of template used to create this table

## VBA Syntax

See [InsertTableNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~InsertTableNotify_EV.html).

## Examples

[Fire Notification When Inserting a Table in a Drawing Document (C#)](Fire_Notification_When_Inserting_a_Table_in_a_Drawing_Document_Example_CSharp.htm)
[Fire Notification When Inserting a Table in a Drawing Document (VB.NET)](Fire_Notification_When_Inserting_a_Table_in_a_Drawing_Document_Example_VBNET.htm)
[Fire Notification When Inserting a Table in a Drawing Document (VBA)](Fire_Notification_When_Inserting_a_Table_in_a_Drawing_Document_Example_VB.htm)

## Remarks

If developing a C++ application, use [swDrawingInsertTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
