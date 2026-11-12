---
title: "DPartDocEvents_DeleteCustomPropertyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DeleteCustomPropertyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteCustomPropertyNotifyEventHandler.html"
---

# DPartDocEvents_DeleteCustomPropertyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the user has deleted a custom property.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DeleteCustomPropertyNotifyEventHandler( _
   ByVal propName As System.String, _
   ByVal Configuration As System.String, _
   ByVal Value As System.String, _
   ByVal valueType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DeleteCustomPropertyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DeleteCustomPropertyNotifyEventHandler(
   System.string propName,
   System.string Configuration,
   System.string Value,
   System.int valueType
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DeleteCustomPropertyNotifyEventHandler(
   System.String^ propName,
   System.String^ Configuration,
   System.String^ Value,
   System.int valueType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `propName`: Name of the deleted property
- `Configuration`: Name of the configuration that contains the property
- `Value`: Value of the deleted property
- `valueType`: Valid type for VARIANT; see Microsoft MSDN for a list of valid VARIANT types

## VBA Syntax

See [DeleteCustomPropertyNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DeleteCustomPropertyNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartDeleteCustomPropertyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
