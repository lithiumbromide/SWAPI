---
title: "DAssemblyDocEvents_ModifyTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ModifyTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ModifyTableNotifyEventHandler.html"
---

# DAssemblyDocEvents_ModifyTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your program when a table has been modified in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ModifyTableNotifyEventHandler( _
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
Dim instance As New DAssemblyDocEvents_ModifyTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ModifyTableNotifyEventHandler(
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
public delegate System.int DAssemblyDocEvents_ModifyTableNotifyEventHandler(
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

See [ModifyTableNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ModifyTableNotify_EV.html).

## Examples

[Fire Notification When Changing a Table in an Assembly Document (C#)](Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_CSharp.htm)
[Fire Notification When Changing a Table in an Assembly Document (VB.NET)](Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_VBNET.htm)
[Fire Notification When Changing a Table in an Assembly Document (VBA)](Fire_Notification_When_Changing_a_Table_in_an_Assembly_Document_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyModifyTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
