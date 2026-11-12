---
title: "ComponentStateChangeNotify - AssemblyDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDocEvents/AssemblyDocEvents__ComponentStateChangeNotify.htm"
---

# ComponentStateChangeNotify - AssemblyDoc Event

This event is obsolete and has been superseded by AssemblyDoc event [ComponentStateChangeNotify2](sldworksAPI.chm::/AssemblyDocEvents/AssemblyDocEvents__ComponentStateChangeNotify2.htm).

Description

This event is fired whenever the state of a component within this assembly changes.

status = ComponentStateChangeNotify ( componentModel , oldCompState , newCompState )

| Input: | (LPDISPATCH) componentModel | Pointer to the component model |
| --- | --- | --- |
| Input: | (short) oldCompState | Previous state of the component |
| Input: | (short) newCompState | New state of the component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks fires this event on this AssemblyDoc even if it is not the active document. However, SolidWorks does not generate this notification if a part is explicitly opened by the user or opened programmatically. In this situation, SolidWorks resolves the component part in any open assembly that references the part. Your application must recognize this by watching for SldWorksEvents::FileOpenNotify.

When a component is resolved or unsuppressed, its ModelDoc object becomes available to your application. Within this notification, you can get this object and register for other events. This might be useful for Project Data Management (PDM) applications that want to ask the user to check out the assembly component if the user tries to make changes.
