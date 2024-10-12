export const ROUTE_CONSTANTS = {
  login: 'login',
  user: 'user',
};

const BASE_PATHS = {
  user: `/${ROUTE_CONSTANTS.user}`,
};

export const PATHS = {
  user: {
    index: BASE_PATHS.user,
    login: `${BASE_PATHS.user}/${ROUTE_CONSTANTS.user}`,
  },
};

export const createDescendantRoute = (route: string) => `${route}/*`;