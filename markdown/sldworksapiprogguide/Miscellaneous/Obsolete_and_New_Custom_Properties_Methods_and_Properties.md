---
title: "Obsolete and New Custom Properties Methods and Properties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Miscellaneous/Obsolete_and_New_Custom_Properties_Methods_and_Properties.htm"
---

# Obsolete and New Custom Properties Methods and Properties

The following list identifies the now obsolete custom property methods and properties and their replacements as of SOLIDWORKS 2007 and later.

| Obsolete API | New API |
| --- | --- |
| IConfiguration APIs IConfiguration::GetCustomProperties IConfiguration::GetCustomPropertiesCount | IConfiguration APIs IConfiguration::CustomPropertyManager |
| ICustomPropertyManager APIs ICustomPropertyManager::Add ICustomPropertyManager::GetType | ICustomPropertyManager APIs ICustomPropertyManager::Add2 ICustomPropertyManager::GetType2 ICustomPropertyManager::GetAll |
| IModelDoc2 APIs IModelDoc2::AddCustomInfo3 IModelDoc2::CustomInfo2 IModelDoc2::DeleteCustomInfo2 IModelDoc2::GetCustomInfoCount2 IModelDoc2::GetCustomInfoNames2 IModelDoc2::GetCustomInfoType3 IModelDoc2::GetCustomInfoValue | IModelDocExtension APIs IModelDocExtension::CustomPropertyManager |
