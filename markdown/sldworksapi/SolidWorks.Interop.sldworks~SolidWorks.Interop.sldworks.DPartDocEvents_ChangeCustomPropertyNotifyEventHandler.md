---
title: "DPartDocEvents_ChangeCustomPropertyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ChangeCustomPropertyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ChangeCustomPropertyNotifyEventHandler.html"
---

# DPartDocEvents_ChangeCustomPropertyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the user has changed a custom property.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ChangeCustomPropertyNotifyEventHandler( _
   ByVal propName As System.String, _
   ByVal Configuration As System.String, _
   ByVal oldValue As System.String, _
   ByVal NewValue As System.String, _
   ByVal valueType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ChangeCustomPropertyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ChangeCustomPropertyNotifyEventHandler(
   System.string propName,
   System.string Configuration,
   System.string oldValue,
   System.string NewValue,
   System.int valueType
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ChangeCustomPropertyNotifyEventHandler(
   System.String^ propName,
   System.String^ Configuration,
   System.String^ oldValue,
   System.String^ NewValue,
   System.int valueType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `propName`: Name of the changed property
- `Configuration`: Configuration that contains the property
- `oldValue`: Previous value of the property
- `NewValue`: New value of the property
- `valueType`: Valid type for VARIANT; see Microsoft MSDN for a list of valid VARIANT types

## VBA Syntax

See [ChangeCustomPropertyNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ChangeCustomPropertyNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartChangeCustomPropertyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this event.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
