---
title: "Feature::GetSpecificFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__GetSpecificFeature.htm"
---

# Feature::GetSpecificFeature

This method is obsolete and has been superseded by [Feature::GetSpecificFeature2](sldworksAPI.chm::/Feature/Feature__GetSpecificFeature2.htm).

Description

This method gets the interface for the specific feature type.

Syntax (OLE Automation)

retval = Feature.GetSpecificFeature ()

| Return: | (LPDISPATCH) retval | Dispatch pointer to a feature of unknown type |
| --- | --- | --- |

Syntax (COM)

status = Feature->IGetSpecificFeature ( &retval )

| Output: | (LPUNKNOWN) retval | Pointer to the feature of unknown type |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

| If... | Then... |
| --- | --- |
| You start with a Feature object and want to get a more specific object | A call to Feature::GetSpecificFeature is required. If you have the more specific object, then a call to QueryInterface in C++ or assignment to a Feature-typed variable allows an application to get back to the Feature object. |
| You are writing a Dispatch application | You can use Feature::GetTypeName to recognize the type of Dispatch object returned so you can call the appropriate properties and methods for that object. |
| You are writing a COM application | You can use the return value with QueryInterface to determine the object returned. |
| No interface exists | This method returns NULL. |

For many feature types, this method returns NULL because there is no specific object for that type (for example, extrusion or cut features). For all functions that return objects, always check whether the return value is NULL before you try to use it.
