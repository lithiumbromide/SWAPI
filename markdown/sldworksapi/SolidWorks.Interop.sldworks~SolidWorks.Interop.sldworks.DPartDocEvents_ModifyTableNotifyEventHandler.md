---
title: "DPartDocEvents_ModifyTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ModifyTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ModifyTableNotifyEventHandler.html"
---

# DPartDocEvents_ModifyTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your program when a table has been modified in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ModifyTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.Integer, _
   ByVal reason As System.Integer, _
   ByVal RowInfo As System.Integer, _
   ByVal ColumnInfo As System.Integer, _
   ByVal DataInfo As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ModifyTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ModifyTableNotifyEventHandler(
   TableAnnotation TableAnnotation,
   System.int TableType,
   System.int reason,
   System.int RowInfo,
   System.int ColumnInfo,
   System.string DataInfo
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ModifyTableNotifyEventHandler(
   TableAnnotation^ TableAnnotation,
   System.int TableType,
   System.int reason,
   System.int RowInfo,
   System.int ColumnInfo,
   System.String^ DataInfo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableAnnotation`: [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)
- `TableType`: Type of table as defined in [swTableAnnotationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableAnnotationType_e.html)
- `reason`: Reason as defined in [swModifyTableNotifyReason_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swModifyTableNotifyReason_e.html)
- `RowInfo`: Index of modified row
- `ColumnInfo`: Index of modified column
- `DataInfo`: Modified string

## VBA Syntax

See [ModifyTableNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ModifyTableNotify_EV.html).

## Examples

[Fire Notification When Changing a Table in a Part Document (C#)](Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_CSharp.htm)
[Fire Notification When Changing a Table in a Part Document (VB.NET)](Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_VBNET.htm)
[Fire Notification When Changing a Table in a Part Document (VBA)](Fire_Notification_When_Changing_a_Table_in_a_Part_Document_Example_VB.htm)

## Remarks

If developing a C++ application, use [swPartModifyTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
