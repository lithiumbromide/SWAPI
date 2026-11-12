---
title: "DDrawingDocEvents_AddCustomPropertyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_AddCustomPropertyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AddCustomPropertyNotifyEventHandler.html"
---

# DDrawingDocEvents_AddCustomPropertyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the user has added a custom property.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_AddCustomPropertyNotifyEventHandler( _
   ByVal propName As System.String, _
   ByVal Configuration As System.String, _
   ByVal Value As System.String, _
   ByVal valueType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_AddCustomPropertyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_AddCustomPropertyNotifyEventHandler(
   System.string propName,
   System.string Configuration,
   System.string Value,
   System.int valueType
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_AddCustomPropertyNotifyEventHandler(
   System.String^ propName,
   System.String^ Configuration,
   System.String^ Value,
   System.int valueType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `propName`: Name of the new custom property
- `Configuration`: Configuration that contains the property
- `Value`: Value of the new property
- `valueType`: Valid type for VARIANT; see Microsoft MSDN for a list of valid VARIANT types

## VBA Syntax

See [AddCustomPropertyNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~AddCustomPropertyNotify_EV.html).

## Remarks

The ValueType argument is one of the valid types that VARIANT can contain.

If developing a C++ application, use [swDrawingAddCustomPropertyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
