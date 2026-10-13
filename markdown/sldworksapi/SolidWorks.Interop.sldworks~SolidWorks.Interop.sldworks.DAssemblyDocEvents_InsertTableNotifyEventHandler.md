---
title: "DAssemblyDocEvents_InsertTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_InsertTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_InsertTableNotifyEventHandler.html"
---

# DAssemblyDocEvents_InsertTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your program when a table has been inserted in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_InsertTableNotifyEventHandler( _
   ByVal TableAnnotation As TableAnnotation, _
   ByVal TableType As System.String, _
   ByVal TemplatePath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_InsertTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_InsertTableNotifyEventHandler(
   TableAnnotation TableAnnotation,
   System.string TableType,
   System.string TemplatePath
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_InsertTableNotifyEventHandler(
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

See [InsertTableNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~InsertTableNotify_EV.html).

## Examples

[Fire Notification When Inserting a Table in an Assembly Document (C#)](Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_CSharp.htm)
[Fire Notification When Inserting a Table in an Assembly Document (VB.NET)](Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_VBNET.htm)
[Fire Notification When Inserting a Table in an Assembly Document (VBA)](Fire_Notification_When_Inserting_a_Table_in_an_Assembly_Document_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyInsertTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
