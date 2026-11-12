---
title: "DAssemblyDocEvents_DeleteItemPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_DeleteItemPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_DeleteItemPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_DeleteItemPreNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_DeleteItemPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_DeleteItemPreNotifyEventHandler(
   System.int EntityType,
   System.string itemName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_DeleteItemPreNotifyEventHandler(
   System.int EntityType,
   System.String^ itemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of entity to delete as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `itemName`: Name of the entity to delete

## VBA Syntax

See [DeleteItemPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~DeleteItemPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyDeleteSelectionPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Use [IAssemblyDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~FeatureByName.html) or [IAssemblyDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IFeatureByName.html) or [IModelDoc2::GetConfigurationByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetConfigurationByName.html) and [IModelDoc2::IGetConfigurationByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html) to get the object being deleted. Use [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get the component.

## Availability

SOLIDWORKS 2005 SP1, Revision 13.1
